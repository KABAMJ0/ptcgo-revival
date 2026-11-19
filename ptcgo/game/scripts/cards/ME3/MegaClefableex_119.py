from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities
from ptcgo.game.session.passives import Passive, carrier_pokemon


class LustrousBodyPassive(Passive):
    """Prevent all effects of your opponent's Pokémon's Abilities done to this Pokémon."""

    def blocks_ability_effects(self, target, carrier):
        return target is carrier_pokemon(carrier)


card = PokemonCardDef(
    guid="ddaa066a-03be-5159-8208-5c794252e6d2",
    key="ME3",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.MegaClefableex.Name",
    display_name="Mega Clefable ex",
    searchable_by=["Mega Clefable ex", "Stage 1", "MEGA", "ex", "MegaClefableex"],
    subtypes=["Stage 1", "MEGA", "ex"],
    collector_number=119,
    set_code="ME3",
    rarity=Rarities.Rare,
    hp=320,
    elements=[PokemonTypes.PSYCHIC],
    stage=PokemonStage.STAGE1,
    retreat_cost=1,
    weakness_type=PokemonTypes.METAL,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Clefairy.Name",
    family_id=35,
    abilities=[
        Ability(
            title="Luminous Wing",
            game_text="Prevent all effects of your opponent's Pok\u00e9mon's Abilities done to this Pok\u00e9mon.",
            passive=LustrousBodyPassive(),
        ),
        Attack(
            title="Shooting Moons",
            game_text="You may discard up to 4 Energy cards from your hand, and this attack does 40 more damage for each card you discarded in this way.",
            cost={PokemonTypes.PSYCHIC: 2},
            damage=120,
            damage_operator="+",
            effect=unimplemented,
        ),
    ],
)