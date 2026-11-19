from ptcgo.game.card_effects.support_common import heal_attack
from ptcgo.game.card_effects.attacks_common import place_counters, count_hand
from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities
from ptcgo.game.card_effects.support_common import heal_attack

card = PokemonCardDef(
    guid="95906460-8d77-58a0-9319-1d042c35e2fc",
    key="SM9",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.MrMimeGX.Name",
    display_name="Mr. Mime-GX",
    searchable_by=["Mr. Mime-GX", "Basic", "GX", "MrMimeGX"],
    subtypes=["Basic", "GX"],
    collector_number=67,
    set_code="SM9",
    rarity=Rarities.RareHolo,
    hp=150,
    elements=[PokemonTypes.PSYCHIC],
    stage=PokemonStage.BASIC,
    retreat_cost=2,
    family_id=122,
    abilities=[
        Ability(
            title="Magic Odds",
            game_text="Prevent all damage done to this Pok\u00e9mon by your opponent's attacks if that damage is exactly 10, 30, 50, 70, 90, 110, 130, 150, 170, 190, 210, 230, or 250.",
            effect=unimplemented,
        ),
        Attack(
            title="Breakdown",
            game_text="For each card in your opponent's hand, put 1 damage counter on their Active Pok\u00e9mon.",
            cost={PokemonTypes.PSYCHIC: 1, PokemonTypes.COLORLESS: 1},
            effect=place_counters(lambda ctx: 1 * count_hand("opponent")(ctx), target="opponent_active"),
        ),
        Attack(
            title="Life Trick-GX",
            game_text="Heal all damage from this Pok\u00e9mon. (You can't use more than 1 GX attack in a game.)",
            cost={PokemonTypes.COLORLESS: 1},
            effect=heal_attack(all_damage=True, target="self"),
        ),
    ],
)