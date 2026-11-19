from ptcgo.game.card_effects.support_common import draw_until_effect
from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="65093e08-def6-592b-a991-dc2379f60391",
    key="PL1",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Blissey.Name",
    display_name="Blissey",
    searchable_by=["Blissey", "Stage 1", "Blissey"],
    subtypes=["Stage 1"],
    collector_number=22,
    set_code="PL1",
    rarity=Rarities.Rare,
    hp=120,
    elements=[PokemonTypes.COLORLESS],
    stage=PokemonStage.STAGE1,
    retreat_cost=2,
    weakness_type=PokemonTypes.FIGHTING,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Chansey.Name",
    family_id=113,
    abilities=[
        Ability(
            title="Nurse Call",
            game_text="Once during your turn (before your attack), you may discard a card from your hand. If you do, remove 2 damage counters from 1 of your Pok\u00e9mon. You can't use more than 1 Nurse Call Pok\u00e9-Power each turn. This power can't be used if Blissey is affected by a Special Condition.",
            effect=draw_until_effect(6),
        ),
        Attack(
            title="Return",
            game_text="Draw cards until you have 6 cards in your hand.",
            cost={PokemonTypes.COLORLESS: 1},
            damage=20,
            effect=unimplemented,
        ),
        Attack(
            title="Double-edge",
            game_text="Blissey does 60 damage to itself.",
            cost={PokemonTypes.COLORLESS: 4},
            damage=100,
            effect=unimplemented,
        ),
    ],
)