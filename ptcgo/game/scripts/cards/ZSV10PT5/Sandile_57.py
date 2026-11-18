from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="1f4cc2d5-24e7-5a0e-aba7-99eefc64bb2b",
    key="ZSV10PT5",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Sandile.Name",
    display_name="Sandile",
    searchable_by=["Sandile", "Basic", "Sandile"],
    subtypes=["Basic"],
    collector_number=57,
    set_code="ZSV10PT5",
    rarity=Rarities.Common,
    hp=70,
    elements=[PokemonTypes.DARKNESS],
    stage=PokemonStage.BASIC,
    retreat_cost=2,
    weakness_type=PokemonTypes.GRASS,
    family_id=551,
    abilities=[
        Attack(
            title="Tighten Up",
            game_text="Your opponent discards a card from their hand.",
            cost={PokemonTypes.DARKNESS: 1},
            damage=10,
            effect=unimplemented,
        ),
    ],
)