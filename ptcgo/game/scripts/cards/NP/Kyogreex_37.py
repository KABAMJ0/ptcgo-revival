from ptcgo.game.card_effects.attacks_common import spread_damage
from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities
from ptcgo.game.card_effects.attacks_common import spread_damage
from ptcgo.game.card_effects.passives_common import composed
from ptcgo.game.card_effects.trainers import is_basic_energy_card
from ptcgo.game.card_effects.support_common import attach_from_hand


card = PokemonCardDef(
    guid="1c23b547-8b26-5dfe-b0c1-bb0ff749fe91",
    key="NP",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Kyogreex.Name",
    display_name="Kyogre ex",
    searchable_by=["Kyogre ex", "Basic", "EX", "Kyogreex"],
    subtypes=["Basic", "EX"],
    collector_number=37,
    set_code="NP",
    rarity=Rarities.RarePromo,
    hp=100,
    elements=[PokemonTypes.WATER],
    stage=PokemonStage.BASIC,
    retreat_cost=2,
    weakness_type=PokemonTypes.LIGHTNING,
    family_id=382,
    abilities=[
        Ability(
            title="Frenzy",
            game_text="As long as your opponent has Groudon, Groudon ex, Rayquaza, or Rayquaza ex in play. Kyogre ex's attacks do 40 more damage to the Defending Pok\u00e9mon (before applying Weakness and Resistance).",
            effect=spread_damage(10, side="opponent", include_active=False),
        ),
        Attack(
            title="Aqua Supply",
            game_text="You may attach a basic Energy card from your hand to 1 of your Pok\u00e9mon.",
            cost={PokemonTypes.WATER: 1, PokemonTypes.COLORLESS: 1},
            damage=30,
            effect=composed(lambda ctx: ctx.deal_damage(), attach_from_hand(is_basic_energy_card, count=1, target='choice', minimum=0)),
        ),
        Attack(
            title="Tsunami",
            game_text="Does 10 damage to each of your opponent's Benched Pok\u00e9mon. (Don't apply Weakness and Resistance for Benched Pok\u00e9mon.)",
            cost={PokemonTypes.WATER: 1, PokemonTypes.COLORLESS: 2},
            damage=40,
            effect=spread_damage(10, side="opponent", include_active=False),
        ),
    ],
)