from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="7cb7de4f-a29b-50b2-ab8f-fb82fe540351",
    key="SVP",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.PikachuwithGreyFeltHat.Name",
    display_name="Pikachu with Grey Felt Hat",
    searchable_by=["Pikachu with Grey Felt Hat", "Basic", "PikachuwithGreyFeltHat"],
    subtypes=["Basic"],
    collector_number=85,
    set_code="SVP",
    rarity=Rarities.RarePromo,
    hp=60,
    elements=[PokemonTypes.LIGHTNING],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIGHTING,
    family_id=25,
    abilities=[
        Attack(
            title="Pika-Portrait",
            game_text="Search your deck for a Pikachu and put it onto your Bench. Then, shuffle your deck.",
            cost={PokemonTypes.LIGHTNING: 1},
            effect=unimplemented,
        ),
    ],
)