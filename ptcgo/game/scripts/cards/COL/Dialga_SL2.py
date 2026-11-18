from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="8f502f8b-536e-5a34-92f7-8b6073428cee",
    key="COL",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Dialga.Name",
    display_name="Dialga",
    searchable_by=["Dialga", "Basic", "Dialga"],
    subtypes=["Basic"],
    collector_number=2,
    set_code="COL",
    rarity=Rarities.RareHolo,
    hp=100,
    elements=[PokemonTypes.METAL],
    stage=PokemonStage.BASIC,
    retreat_cost=3,
    weakness_type=PokemonTypes.FIRE,
    resistance_type=PokemonTypes.PSYCHIC,
    family_id=483,
    abilities=[
        Attack(
            title="Time Rewind",
            game_text="Shuffle your hand into your deck.",
            cost={PokemonTypes.METAL: 4},
            damage=70,
            effect=unimplemented,
        ),
    ],
)