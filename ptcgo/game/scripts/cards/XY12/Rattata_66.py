from ptcgo.game.card_effects.trainers import discard_tools
from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented, Triggers
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="8508fd09-24c1-59d3-b17d-c7af8e24e563",
    key="XY12",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Rattata.Name",
    display_name="Rattata",
    searchable_by=["Rattata", "Basic", "Rattata"],
    subtypes=["Basic"],
    collector_number=66,
    set_code="XY12",
    rarity=Rarities.Common,
    hp=40,
    elements=[PokemonTypes.COLORLESS],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIGHTING,
    family_id=19,
    abilities=[
        Ability(
            title="Mischievous Fang",
            game_text="When you play this Pok\u00e9mon from your hand onto your Bench, you may discard all Pok\u00e9mon Tool cards attached to your opponent's Active Pok\u00e9mon.",
            trigger=Triggers.ON_PLAY,
            effect=discard_tools(count=99, sides="theirs"),
        ),
        Attack(
            title="Bite",
            cost={PokemonTypes.COLORLESS: 1},
            damage=10,
        ),
    ],
)