from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities
from ptcgo.game.card_effects.attacks_common import bonus_if


def _fewer_in_play(ctx) -> bool:
    return len(ctx.my_pokemon_in_play()) < len(ctx.opponent_pokemon_in_play())


async def clanging_scales(ctx):
    """Printed damage; during the opponent's next turn this Pokemon takes 30
    more damage from attacks."""
    await ctx.deal_damage()
    if ctx.attacker is not None:
        ctx.add_damage_taken_modifier(30, ctx.attacker,
                                      through="opponent_next_turn")


card = PokemonCardDef(
    guid="df1d9c4c-1642-5307-a7d6-4cab0872af1d",
    key="SM4",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Kommoo.Name",
    display_name="Kommo-o",
    searchable_by=["Kommo-o", "Stage 2", "Kommoo"],
    subtypes=["Stage 2"],
    collector_number=77,
    set_code="SM4",
    rarity=Rarities.Rare,
    hp=160,
    elements=[PokemonTypes.DRAGON],
    stage=PokemonStage.STAGE2,
    retreat_cost=2,
    weakness_type=PokemonTypes.FAIRY,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Hakamoo.Name",
    family_id=782,
    abilities=[
        Attack(
            title="War Cry",
            game_text="If you have fewer Pok\u00e9mon in play than your opponent, this attack does 90 more damage.",
            cost={PokemonTypes.COLORLESS: 2},
            damage=30,
            damage_operator="+",
            effect=bonus_if(_fewer_in_play, 90),
        ),
        Attack(
            title="Clanging Scales",
            game_text="During your opponent's next turn, this Pok\u00e9mon takes 30 more damage from attacks (after applying Weakness and Resistance).",
            cost={PokemonTypes.LIGHTNING: 1, PokemonTypes.FIGHTING: 1, PokemonTypes.COLORLESS: 1},
            damage=130,
            effect=clanging_scales,
        ),
    ],
)