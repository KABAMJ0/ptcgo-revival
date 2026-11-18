from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="6e75805e-fa49-5fcd-9db4-9521520debfe",
    key="HGSS1",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Cleffa.Name",
    display_name="Cleffa",
    searchable_by=["Cleffa", "Basic", "Cleffa"],
    subtypes=["Basic"],
    collector_number=17,
    set_code="HGSS1",
    rarity=Rarities.Rare,
    hp=30,
    elements=[PokemonTypes.COLORLESS],
    stage=PokemonStage.BASIC,
    retreat_cost=0,
    family_id=173,
    abilities=[
        Ability(
            title="Sweet Sleeping Face",
            game_text="As long as Cleffa is Asleep, prevent all damage done to Cleffa by attacks.",
            effect=unimplemented,
        ),
        Attack(
            title="Eeeeeeek",
            game_text="Shuffle your hand into your deck, then draw 6 cards. Cleffa is now Asleep.",
            cost={},
            effect=unimplemented,
        ),
    ],
)