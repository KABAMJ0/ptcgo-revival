from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities
from ptcgo.game.card_effects.attacks_common import ignore_modifier_attack

card = PokemonCardDef(
    guid="b3e59361-d246-5221-9819-0f47e82e28b0",
    key="SM3",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.NecrozmaGX.Name",
    display_name="Necrozma-GX",
    searchable_by=["Necrozma-GX", "Basic", "GX", "NecrozmaGX"],
    subtypes=["Basic", "GX"],
    collector_number=63,
    set_code="SM3",
    rarity=Rarities.RareHolo,
    hp=180,
    elements=[PokemonTypes.PSYCHIC],
    stage=PokemonStage.BASIC,
    retreat_cost=2,
    weakness_type=PokemonTypes.PSYCHIC,
    family_id=800,
    abilities=[
        Ability(
            title="Light's End",
            game_text="Prevent all damage done to this Pok\u00e9mon by attacks from Colorless Pok\u00e9mon.",
            effect=unimplemented,
        ),
        Attack(
            title="Prismatic Burst",
            game_text="Discard all Psychic Energy from this Pok\u00e9mon. This attack does 60 more damage for each card you discarded in this way.",
            cost={PokemonTypes.COLORLESS: 3},
            damage=10,
            damage_operator="+",
            effect=unimplemented,
        ),
        Attack(
            title="Black Ray-GX",
            game_text="This attack does 100 damage to each of your opponent's Pok\u00e9mon-GX and Pok\u00e9mon-EX. This damage isn't affected by Weakness or Resistance. (You can't use more than 1 GX attack in a game.)",
            cost={PokemonTypes.COLORLESS: 3},
            effect=ignore_modifier_attack(ignore_weakness=True, ignore_resistance=True),
        ),
    ],
)