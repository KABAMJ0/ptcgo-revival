from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="f96038fc-e18c-5ace-9310-3ef26dddac50",
    key="ZSV10PT5",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Golurk.Name",
    display_name="Golurk",
    searchable_by=["Golurk", "Stage 1", "Golurk"],
    subtypes=["Stage 1"],
    collector_number=43,
    set_code="ZSV10PT5",
    rarity=Rarities.Uncommon,
    hp=160,
    elements=[PokemonTypes.PSYCHIC],
    stage=PokemonStage.STAGE1,
    retreat_cost=4,
    weakness_type=PokemonTypes.DARKNESS,
    resistance_type=PokemonTypes.FIGHTING,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Golett.Name",
    family_id=622,
    abilities=[
        Attack(
            title="Double Smash",
            game_text="Flip 2 coins. This attack does 80 damage for each heads.",
            cost={PokemonTypes.COLORLESS: 3},
            damage=80,
            damage_operator="x",
            effect=unimplemented,
        ),
        Attack(
            title="Golurk Hammer",
            cost={PokemonTypes.PSYCHIC: 2, PokemonTypes.COLORLESS: 3},
            damage=200,
        ),
    ],
)