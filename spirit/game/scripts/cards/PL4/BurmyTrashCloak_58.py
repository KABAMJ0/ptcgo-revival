from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="03e29e98-f84f-5005-887d-ec0a37f3ebe3",
    key="PL4",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.BurmyTrashCloak.Name",
    display_name="Burmy Trash Cloak",
    searchable_by=["Burmy Trash Cloak", "Basic", "BurmyTrashCloak"],
    subtypes=["Basic"],
    collector_number=58,
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
            game_text="Burmy Trash Cloak can evolve during the turn you play it.",
            effect=unimplemented,
        ),
        Attack(
            title="Tackle",
            cost={PokemonTypes.METAL: 1, PokemonTypes.COLORLESS: 1},
            damage=20,
        ),
    ],
)