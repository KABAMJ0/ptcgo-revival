from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, Activations, unimplemented
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities
from ptcgo.game.card_effects.support_common import discard_then_draw

card = PokemonCardDef(
    guid="00186787-1b98-5c17-8692-3a41744d2d0c",
    key="SWSH12TG",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Gardevoir.Name",
    display_name="Gardevoir",
    searchable_by=["Gardevoir", "Stage 2", "Gardevoir"],
    subtypes=["Stage 2"],
    collector_number=5,
    set_code="SWSH12TG",
    rarity=Rarities.RareHolo,
    hp=150,
    elements=[PokemonTypes.PSYCHIC],
    stage=PokemonStage.STAGE2,
    retreat_cost=2,
    weakness_type=PokemonTypes.METAL,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Kirlia.Name",
    family_id=282,
    abilities=[
        Ability(
            title="Refinement",
            game_text="You must discard a card from your hand in order to use this Ability. Once during your turn, you may draw 2 cards.",
            activation=Activations.ONCE_PER_TURN,
            effect=discard_then_draw(1, 2),
        ),
        Attack(
            title="Magical Shot",
            cost={PokemonTypes.PSYCHIC: 1, PokemonTypes.COLORLESS: 1},
            damage=120,
        ),
    ],
)