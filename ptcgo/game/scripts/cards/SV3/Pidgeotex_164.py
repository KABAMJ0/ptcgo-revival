from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented, Activations
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities
from ptcgo.game.card_effects.support_common import search_to_hand

card = PokemonCardDef(
    guid="b3666e0b-18e0-54db-bd64-00de3d6b2b25",
    key="SV3",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Pidgeotex.Name",
    display_name="Pidgeot ex",
    searchable_by=["Pidgeot ex", "Stage 2", "ex", "Pidgeotex"],
    subtypes=["Stage 2", "ex"],
    collector_number=164,
    set_code="SV3",
    rarity=Rarities.Rare,
    hp=280,
    elements=[PokemonTypes.COLORLESS],
    stage=PokemonStage.STAGE2,
    retreat_cost=0,
    weakness_type=PokemonTypes.LIGHTNING,
    resistance_type=PokemonTypes.FIGHTING,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Pidgeotto.Name",
    family_id=16,
    abilities=[
        Ability(
            title="Quick Search",
            game_text="Once during your turn, you may search your deck for a card and put it into your hand. Then, shuffle your deck. You can't use more than 1 Quick Search Ability each turn.",
            activation=Activations.ONCE_PER_TURN,
            effect=search_to_hand(count=1, minimum=0),
        ),
        Attack(
            title="Blustery Wind",
            game_text="You may discard a Stadium in play.",
            cost={PokemonTypes.COLORLESS: 2},
            damage=120,
            effect=unimplemented,
        ),
    ],
)