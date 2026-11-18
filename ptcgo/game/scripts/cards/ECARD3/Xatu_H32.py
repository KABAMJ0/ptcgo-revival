from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="c01711e7-dc16-5eef-a1df-a03d8624d4fb",
    key="ECARD3",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Xatu.Name",
    display_name="Xatu",
    searchable_by=["Xatu", "Stage 1", "Xatu"],
    subtypes=["Stage 1"],
    collector_number=32,
    set_code="ECARD3",
    rarity=Rarities.RareHolo,
    hp=80,
    elements=[PokemonTypes.PSYCHIC],
    stage=PokemonStage.STAGE1,
    retreat_cost=1,
    weakness_type=PokemonTypes.PSYCHIC,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Natu.Name",
    family_id=177,
    abilities=[
        Ability(
            title="Synchronicity",
            game_text="You may attach any Technical Machine to Xatu.",
            effect=unimplemented,
        ),
        Attack(
            title="Warp Hole",
            game_text="Flip a coin. If heads, choose a card from your discard pile and put it on top of your deck.",
            cost={PokemonTypes.COLORLESS: 3},
            damage=30,
            effect=unimplemented,
        ),
    ],
)