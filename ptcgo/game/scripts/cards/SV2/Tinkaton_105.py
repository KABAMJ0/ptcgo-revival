from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, Activations, unimplemented
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities
from ptcgo.game.card_effects.support_common import discard_then_draw

card = PokemonCardDef(
    guid="c52bdf00-812f-5820-b122-a121b5a41e90",
    key="SV2",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Tinkaton.Name",
    display_name="Tinkaton",
    searchable_by=["Tinkaton", "Stage 2", "Tinkaton"],
    subtypes=["Stage 2"],
    collector_number=105,
    set_code="SV2",
    rarity=Rarities.Rare,
    hp=140,
    elements=[PokemonTypes.PSYCHIC],
    stage=PokemonStage.STAGE2,
    retreat_cost=2,
    weakness_type=PokemonTypes.METAL,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Tinkatuff.Name",
    family_id=957,
    abilities=[
        Ability(
            title="Gather Materials",
            game_text="You must discard a card from your hand in order to use this Ability. Once during your turn, you may draw 3 cards.",
            activation=Activations.ONCE_PER_TURN,
            effect=discard_then_draw(1, 3),
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