from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="6a7ceb94-b042-5f68-8f17-84c531a659df",
    key="SVP",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Tinkaton.Name",
    display_name="Tinkaton",
    searchable_by=["Tinkaton", "Stage 2", "Tinkaton"],
    subtypes=["Stage 2"],
    collector_number=20,
    set_code="SVP",
    rarity=Rarities.RarePromo,
    hp=140,
    elements=[PokemonTypes.PSYCHIC],
    stage=PokemonStage.STAGE2,
    retreat_cost=2,
    weakness_type=PokemonTypes.METAL,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Tinkatuff.Name",
    family_id=959,
    abilities=[
        Ability(
            title="Gather Materials",
            game_text="You must discard a card from your hand in order to use this Ability. Once during your turn, you may draw 3 cards.",
            effect=unimplemented,
        ),
        Attack(
            title="Special Hammer",
            game_text="If this Pok\u00e9mon has any Special Energy attached, this attack does 90 more damage.",
            cost={PokemonTypes.PSYCHIC: 1, PokemonTypes.COLORLESS: 1},
            damage=90,
            damage_operator="+",
            effect=unimplemented,
        ),
    ],
)