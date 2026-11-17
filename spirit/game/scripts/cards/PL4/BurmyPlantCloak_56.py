from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="9cb8681a-4b12-5695-a83e-7cd54bc49f77",
    key="PL4",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.BurmyPlantCloak.Name",
    display_name="Burmy Plant Cloak",
    searchable_by=["Burmy Plant Cloak", "Basic", "BurmyPlantCloak"],
    subtypes=["Basic"],
    collector_number=56,
    set_code="PL4",
    rarity=Rarities.Common,
    hp=40,
    elements=[PokemonTypes.GRASS],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIRE,
    family_id=412,
    abilities=[
        Ability(
            title="Cloak Evolution",
            game_text="Burmy Plant Cloak can evolve during the turn you play it.",
            effect=unimplemented,
        ),
        Attack(
            title="Tackle",
            cost={PokemonTypes.GRASS: 1, PokemonTypes.COLORLESS: 1},
            damage=20,
        ),
    ],
)