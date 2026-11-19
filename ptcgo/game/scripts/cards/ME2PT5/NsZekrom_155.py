from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities
from ptcgo.game.card_effects.attacks_common import ignore_modifier_attack
from ptcgo.game.card_effects.attacks_common import lock_self_attack


card = PokemonCardDef(
    guid="b66e01d7-a226-5bca-8f6a-7ddcd5a50d4d",
    key="ME2PT5",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.NsZekrom.Name",
    display_name="N's Zekrom",
    searchable_by=["N's Zekrom", "Basic", "NsZekrom"],
    subtypes=["Basic"],
    collector_number=155,
    set_code="ME2PT5",
    rarity=Rarities.Rare,
    hp=130,
    elements=[PokemonTypes.DRAGON],
    stage=PokemonStage.BASIC,
    retreat_cost=2,
    family_id=644,
    abilities=[
        Attack(
            title="Shred",
            game_text="This attack's damage isn't affected by any effects on your opponent's Active Pok\u00e9mon.",
            cost={PokemonTypes.COLORLESS: 3},
            damage=70,
            effect=ignore_modifier_attack(ignore_target_effects=True),
        ),
        Attack(
            title="Rampaging Thunder",
            game_text="During your next turn, this Pok\u00e9mon can't use attacks.",
            cost={PokemonTypes.FIRE: 1, PokemonTypes.LIGHTNING: 2, PokemonTypes.COLORLESS: 1},
            damage=250,
            effect=lock_self_attack(),
        ),
    ],
)