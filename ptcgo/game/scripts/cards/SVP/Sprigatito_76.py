from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="7284b74d-7b22-54e9-ba29-f1a877f344ae",
    key="SVP",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Sprigatito.Name",
    display_name="Sprigatito",
    searchable_by=["Sprigatito", "Basic", "Sprigatito"],
    subtypes=["Basic"],
    collector_number=76,
    set_code="SVP",
    rarity=Rarities.RarePromo,
    hp=60,
    elements=[PokemonTypes.GRASS],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIRE,
    family_id=906,
    abilities=[
        Attack(
            title="Gather Sunlight",
            game_text="Search your deck for up to 2 Basic Energy cards, reveal them, and put them into your hand. Then, shuffle your deck.",
            cost={PokemonTypes.GRASS: 1},
            effect=unimplemented,
        ),
        Attack(
            title="Seed Bomb",
            cost={PokemonTypes.GRASS: 1},
            damage=10,
        ),
    ],
)