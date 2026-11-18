from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="b46ec30c-936a-555d-88ff-d4241c114d59",
    key="ME1",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Spiritomb.Name",
    display_name="Spiritomb",
    searchable_by=["Spiritomb", "Basic", "Spiritomb"],
    subtypes=["Basic"],
    collector_number=148,
    set_code="ME1",
    rarity=Rarities.Rare,
    hp=80,
    elements=[PokemonTypes.DARKNESS],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.GRASS,
    family_id=442,
    abilities=[
        Ability(
            title="Spiteful Swirl",
            game_text="If your Active Darkness Pok\u00e9mon is damaged by an attack from your opponent's Pok\u00e9mon (even if your Active Darkness Pok\u00e9mon is Knocked Out), place 1 damage counter on the Attacking Pok\u00e9mon.",
            effect=unimplemented,
        ),
        Attack(
            title="Mountain Breaker",
            game_text="Discard the top card of your opponent's deck.",
            cost={PokemonTypes.DARKNESS: 1},
            damage=10,
            effect=unimplemented,
        ),
    ],
)