from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="f690bb93-96c6-5f35-ae92-48962a0602ac",
    key="SM7",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Manectric.Name",
    display_name="Manectric",
    searchable_by=["Manectric", "Stage 1", "Manectric"],
    subtypes=["Stage 1"],
    collector_number=52,
    set_code="SM7",
    rarity=Rarities.Rare,
    hp=110,
    elements=[PokemonTypes.LIGHTNING],
    stage=PokemonStage.STAGE1,
    retreat_cost=0,
    weakness_type=PokemonTypes.FIGHTING,
    resistance_type=PokemonTypes.METAL,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Electrike.Name",
    family_id=309,
    abilities=[
        Ability(
            title="Electric Start",
            game_text="If you go second, and if this Pok\u00e9mon is in your hand when you are setting up to play, you may put it face down as your Active Pok\u00e9mon or on your Bench.",
            effect=unimplemented,
        ),
        Attack(
            title="Double Charge",
            game_text="You may attach up to 2 basic Energy cards from your hand to 1 of your Benched Pok\u00e9mon.",
            cost={PokemonTypes.LIGHTNING: 1},
            damage=40,
            effect=unimplemented,
        ),
    ],
)