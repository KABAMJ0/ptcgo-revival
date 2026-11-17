from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="039d5d9c-4ca8-577c-9e8f-83211d54d37a",
    key="PL4",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.BurmySandyCloak.Name",
    display_name="Burmy Sandy Cloak",
    searchable_by=["Burmy Sandy Cloak", "Basic", "BurmySandyCloak"],
    subtypes=["Basic"],
    collector_number=57,
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
            game_text="Burmy Sandy Cloak can evolve during the turn you play it.",
            effect=unimplemented,
        ),
        Attack(
            title="Tackle",
            cost={PokemonTypes.FIGHTING: 1, PokemonTypes.COLORLESS: 1},
            damage=20,
        ),
    ],
)