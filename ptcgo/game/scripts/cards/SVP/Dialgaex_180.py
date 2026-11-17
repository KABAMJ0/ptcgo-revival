from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="3d4eca34-6a75-5a7d-a4e8-5ea780258b46",
    key="SVP",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Dialgaex.Name",
    display_name="Dialga ex",
    searchable_by=["Dialga ex", "Basic", "ex", "Dialgaex"],
    subtypes=["Basic", "ex"],
    collector_number=180,
    set_code="SVP",
    rarity=Rarities.RarePromo,
    hp=220,
    elements=[PokemonTypes.METAL],
    stage=PokemonStage.BASIC,
    retreat_cost=2,
    weakness_type=PokemonTypes.FIRE,
    resistance_type=PokemonTypes.GRASS,
    family_id=483,
    abilities=[
        Attack(
            title="Time Bellow",
            game_text="Draw a card.",
            cost={PokemonTypes.METAL: 1},
            damage=20,
            effect=unimplemented,
        ),
        Attack(
            title="Metal Blast",
            game_text="This attack does 20 more damage for each Metal Energy attached to this Pok\u00e9mon.",
            cost={PokemonTypes.COLORLESS: 3},
            damage=100,
            damage_operator="+",
            effect=unimplemented,
        ),
    ],
)