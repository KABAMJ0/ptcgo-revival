from ptcgo.game.card_effects.attacks_common import mill_attack
from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="df1bea7a-46c3-5bd6-95b3-cad6af80d5bf",
    key="SV3PT5",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Kingler.Name",
    display_name="Kingler",
    searchable_by=["Kingler", "Stage 1", "Kingler"],
    subtypes=["Stage 1"],
    collector_number=99,
    set_code="SV3PT5",
    rarity=Rarities.Uncommon,
    hp=140,
    elements=[PokemonTypes.WATER],
    stage=PokemonStage.STAGE1,
    retreat_cost=3,
    weakness_type=PokemonTypes.LIGHTNING,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Krabby.Name",
    family_id=98,
    abilities=[
        Attack(
            title="Hammer Arm",
            game_text="Discard the top card of your opponent's deck.",
            cost={PokemonTypes.WATER: 3},
            damage=90,
            effect=mill_attack(1),
        ),
        Attack(
            title="Guillotine",
            cost={PokemonTypes.WATER: 4},
            damage=220,
        ),
    ],
)