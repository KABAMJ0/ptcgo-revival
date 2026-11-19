from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities
from ptcgo.game.session.passives import Passive, carrier_pokemon


class LustrousBodyPassive(Passive):
    """Prevent all effects of your opponent's Pokémon's Abilities done to this Pokémon."""

    def blocks_ability_effects(self, target, carrier):
        return target is carrier_pokemon(carrier)


async def gmax_hurricane(ctx):
    """Printed damage, then this attack is locked through the user's next turn."""
    await ctx.deal_damage()
    ability = ctx.ability
    if ctx.attacker is not None and ability is not None and ability.ability_id:
        ctx.session.turn_state.lock_attack(ctx.attacker.entity_id,
                                          ability.ability_id)

card = PokemonCardDef(
    guid="39bbdcf8-5d31-50f2-80fd-cb3a24e09360",
    key="SWSH12TG",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.CorviknightVMAX.Name",
    display_name="Corviknight VMAX",
    searchable_by=["Corviknight VMAX", "VMAX", "CorviknightVMAX"],
    subtypes=["VMAX"],
    collector_number=19,
    set_code="SWSH12TG",
    rarity=Rarities.RareHoloVMAX,
    hp=320,
    elements=[PokemonTypes.METAL],
    stage=PokemonStage.VMAX,
    retreat_cost=0,
    weakness_type=PokemonTypes.FIRE,
    resistance_type=PokemonTypes.GRASS,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.CorviknightV.Name",
    family_id=823,
    abilities=[
        Ability(
            title="Lustrous Body",
            game_text="Prevent all effects of your opponent's Pok\u00e9mon's Abilities done to this Pok\u00e9mon.",
            passive=LustrousBodyPassive(),
        ),
        Attack(
            title="G-Max Hurricane",
            game_text="During your next turn, this Pok\u00e9mon can't use G-Max Hurricane.",
            cost={PokemonTypes.METAL: 2, PokemonTypes.COLORLESS: 1},
            damage=240,
            locks_next_turn=True,
            effect=gmax_hurricane,
        ),
    ],
)