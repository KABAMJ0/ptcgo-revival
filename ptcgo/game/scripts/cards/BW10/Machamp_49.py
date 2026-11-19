from ptcgo.game.card_effects.passives_common import no_resistance_passive
from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from ptcgo.game.attributes import AttrID, PokemonTypes, PokemonStage, Rarities


async def close_combat(ctx) -> None:
    """120 damage; on tails this Pokemon takes 30 more attack damage during
    the opponent's next turn."""
    await ctx.deal_damage()
    heads = await ctx.flip_coins(1, ctx.ability.title)
    if heads and not heads[0]:
        ctx.add_damage_taken_modifier(30, ctx.attacker,
                                      through="opponent_next_turn")


def _fighting_team_attacks(calc, carrier) -> bool:
    """The carrier owner's Fighting Pokemon are attacking."""
    attacker = calc.attacker
    if attacker is None or attacker.owning_player_id != carrier.owning_player_id:
        return False
    return PokemonTypes.FIGHTING.value in (
        attacker.get_attribute(AttrID.POKEMON_TYPES) or [])


card = PokemonCardDef(
    guid="08bc8462-2a4f-5aec-b25e-00d00b574810",
    key="BW10",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Machamp.Name",
    display_name="Machamp",
    searchable_by=["Machamp", "Stage 2", "Machamp"],
    subtypes=["Stage 2"],
    collector_number=49,
    set_code="BW10",
    rarity=Rarities.RareHolo,
    hp=150,
    elements=[PokemonTypes.FIGHTING],
    stage=PokemonStage.STAGE2,
    retreat_cost=3,
    weakness_type=PokemonTypes.PSYCHIC,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Machoke.Name",
    family_id=66,
    abilities=[
        Ability(
            title="Badge of Discipline",
            game_text="The damage of each of your Fighting Pok\u00e9mon's attacks isn't affected by Resistance.",
            passive=no_resistance_passive(when=_fighting_team_attacks),
        ),
        Attack(
            title="Close Combat",
            game_text="Flip a coin. If tails, during your opponent's next turn, any damage done to this Pok\u00e9mon by attacks is increased by 30 (after applying Weakness and Resistance).",
            cost={PokemonTypes.FIGHTING: 1, PokemonTypes.COLORLESS: 3},
            damage=120,
            effect=close_combat,
        ),
    ],
)