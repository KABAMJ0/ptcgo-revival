from ptcgo.game.card_effects.support_common import attach_from_hand
from ptcgo.game.card_effects.trainers import basic_energy_of
from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="951cd7a4-7557-5e6c-8636-311ade4a0bc5",
    key="SM6",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Skiddo.Name",
    display_name="Skiddo",
    searchable_by=["Skiddo", "Basic", "Skiddo"],
    subtypes=["Basic"],
    collector_number=9,
    set_code="SM6",
    rarity=Rarities.Common,
    hp=70,
    elements=[PokemonTypes.GRASS],
    stage=PokemonStage.BASIC,
    retreat_cost=2,
    weakness_type=PokemonTypes.FIRE,
    family_id=672,
    abilities=[
        Attack(
            title="Growth",
            game_text="Attach a Grass Energy card from your hand to this Pok\u00e9mon.",
            cost={PokemonTypes.GRASS: 1},
            effect=attach_from_hand(basic_energy_of("grass"), count=1, target="self"),
        ),
        Attack(
            title="Razor Leaf",
            cost={PokemonTypes.GRASS: 1, PokemonTypes.COLORLESS: 2},
            damage=40,
        ),
    ],
)