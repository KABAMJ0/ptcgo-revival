from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="50cc5fe5-5d1e-5dc6-8a4c-7a9d67f1e729",
    key="NEO2",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.UnownE.Name",
    display_name="Unown [E]",
    searchable_by=["Unown [E]", "Basic", "UnownE"],
    subtypes=["Basic"],
    collector_number=67,
    set_code="NEO2",
    rarity=Rarities.Common,
    hp=40,
    elements=[PokemonTypes.PSYCHIC],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.PSYCHIC,
    family_id=201,
    abilities=[
        Ability(
            title="[Engage]",
            game_text="When you play Unown [E] from your hand, your opponent may shuffle his or her hand into his or her deck and then draw 4 cards. Either way, you may shuffle your hand into your deck and draw 4 cards.",
            effect=unimplemented,
        ),
        Attack(
            title="Hidden Power",
            cost={PokemonTypes.PSYCHIC: 1},
            damage=10,
        ),
    ],
)