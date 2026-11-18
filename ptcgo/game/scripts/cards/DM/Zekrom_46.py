from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities
from ptcgo.game.card_effects.attacks_common import ignore_modifier_attack

card = PokemonCardDef(
    guid="f1ee8565-5428-5f43-aadd-e9d823c3f386",
    key="DM",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Zekrom.Name",
    display_name="Zekrom",
    searchable_by=["Zekrom", "Basic", "Zekrom"],
    subtypes=["Basic"],
    collector_number=46,
    set_code="DM",
    rarity=Rarities.RareHolo,
    hp=130,
    elements=[PokemonTypes.DRAGON],
    stage=PokemonStage.BASIC,
    retreat_cost=3,
    weakness_type=PokemonTypes.FAIRY,
    family_id=644,
    abilities=[
        Attack(
            title="Shred",
            game_text="This attack's damage isn't affected by any effects on your opponent's Active Pok\u00e9mon.",
            cost={PokemonTypes.LIGHTNING: 1, PokemonTypes.COLORLESS: 2},
            damage=70,
            effect=ignore_modifier_attack(ignore_target_effects=True),
        ),
        Attack(
            title="Bolt Strike",
            game_text="Flip a coin. If tails, this Pok\u00e9mon does 50 damage to itself.",
            cost={PokemonTypes.LIGHTNING: 2, PokemonTypes.COLORLESS: 2},
            damage=150,
            effect=unimplemented,
        ),
    ],
)