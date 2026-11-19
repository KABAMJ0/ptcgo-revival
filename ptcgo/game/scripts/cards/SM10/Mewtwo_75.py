from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities
from ptcgo.game.card_effects.attacks_common import ignore_modifier_attack

card = PokemonCardDef(
    guid="9aaff3a9-54b5-5ff8-8fdd-721031ff20e5",
    key="SM10",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Mewtwo.Name",
    display_name="Mewtwo",
    searchable_by=["Mewtwo", "Basic", "Mewtwo"],
    subtypes=["Basic"],
    collector_number=75,
    set_code="SM10",
    rarity=Rarities.Rare,
    hp=120,
    elements=[PokemonTypes.PSYCHIC],
    stage=PokemonStage.BASIC,
    retreat_cost=2,
    weakness_type=PokemonTypes.PSYCHIC,
    family_id=150,
    abilities=[
        Ability(
            title="Mind Report",
            game_text="When you play this Pok\u00e9mon from your hand onto your Bench during your turn, you may put a Supporter card from your discard pile on top of your deck.",
            effect=unimplemented,
        ),
        Attack(
            title="Psyshock",
            game_text="This attack's damage isn't affected by any effects on your opponent's Active Pok\u00e9mon.",
            cost={PokemonTypes.PSYCHIC: 1, PokemonTypes.COLORLESS: 2},
            damage=70,
            effect=ignore_modifier_attack(ignore_target_effects=True),
        ),
    ],
)