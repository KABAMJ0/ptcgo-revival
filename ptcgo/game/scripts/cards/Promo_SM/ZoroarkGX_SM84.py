from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities
from ptcgo.game.card_effects.attacks_common import count_in_play, damage_per
from ptcgo.game.card_effects.support_common import discard_then_draw

card = PokemonCardDef(
    guid="aaba0884-c9a2-5923-b198-ede80a796e53",
    key="Promo_SM",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.ZoroarkGX.Name",
    display_name="Zoroark-GX",
    searchable_by=["Zoroark-GX", "Stage 1", "GX", "ZoroarkGX"],
    subtypes=["Stage 1", "GX"],
    collector_number=84,
    set_code="Promo_SM",
    rarity=Rarities.RarePromo,
    hp=210,
    elements=[PokemonTypes.DARKNESS],
    stage=PokemonStage.STAGE1,
    retreat_cost=2,
    weakness_type=PokemonTypes.FIGHTING,
    resistance_type=PokemonTypes.PSYCHIC,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Zorua.Name",
    family_id=570,
    abilities=[
        Ability(
            title="Trade",
            game_text="Once during your turn (before your attack), you may discard a card from your hand. If you do, draw 2 cards.",
            effect=discard_then_draw(1, 2, optional=False),
        ),
        Attack(
            title="Riotous Beating",
            game_text="This attack does 20 damage for each of your Pok\u00e9mon in play.",
            cost={PokemonTypes.COLORLESS: 2},
            damage=20,
            damage_operator="x",
            effect=damage_per(count_in_play("mine"), 20),
        ),
        Attack(
            title="Trickster-GX",
            game_text="Choose 1 of your opponent's Pok\u00e9mon's attacks and use it as this attack. (You can't use more than 1 GX attack in a game.)",
            cost={PokemonTypes.DARKNESS: 2},
            effect=unimplemented,
        ),
    ],
)