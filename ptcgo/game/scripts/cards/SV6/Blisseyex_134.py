from ptcgo.game.card_effects.attacks_common import energy_move_attack
from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities
from ptcgo.game.card_effects.support_common import draw_until_effect


card = PokemonCardDef(
    guid="4374c765-4989-5939-8354-188c315d4c4f",
    key="SV6",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Blisseyex.Name",
    display_name="Blissey ex",
    searchable_by=["Blissey ex", "Stage 1", "ex", "Blisseyex"],
    subtypes=["Stage 1", "ex"],
    collector_number=134,
    set_code="SV6",
    rarity=Rarities.Rare,
    hp=300,
    elements=[PokemonTypes.COLORLESS],
    stage=PokemonStage.STAGE1,
    retreat_cost=4,
    weakness_type=PokemonTypes.FIGHTING,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Chansey.Name",
    family_id=113,
    abilities=[
        Ability(
            title="Happy Switch",
            game_text="Once during your turn, you may move a Basic Energy from 1 of your Pok\u00e9mon to another of your Pok\u00e9mon.",
            effect=energy_move_attack(1),
        ),
        Attack(
            title="Return",
            game_text="You may draw cards until you have 6 cards in your hand.",
            cost={PokemonTypes.COLORLESS: 3},
            damage=180,
            effect=draw_until_effect(6, optional=True),
        ),
    ],
)