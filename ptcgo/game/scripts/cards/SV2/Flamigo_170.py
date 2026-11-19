from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, Triggers, unimplemented
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities
from ptcgo.game.card_effects.support_common import search_to_hand
from ptcgo.game.card_effects.support_common import entity_name

_named_exact = lambda *names: (
    lambda card: entity_name(card).lower() in {name.lower() for name in names}
)


card = PokemonCardDef(
    guid="697cd5b9-69da-544a-bf79-704bacd7425c",
    key="SV2",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Flamigo.Name",
    display_name="Flamigo",
    searchable_by=["Flamigo", "Basic", "Flamigo"],
    subtypes=["Basic"],
    collector_number=170,
    set_code="SV2",
    rarity=Rarities.Uncommon,
    hp=110,
    elements=[PokemonTypes.COLORLESS],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.LIGHTNING,
    resistance_type=PokemonTypes.FIGHTING,
    family_id=973,
    abilities=[
        Ability(
            title="Insta-Flock",
            game_text="When you play this Pok\u00e9mon from your hand onto your Bench during your turn, you may search your deck for up to 3 Flamigo, reveal them, and put them into your hand. Then, shuffle your deck.",
            trigger=Triggers.ON_PLAY,
            effect=search_to_hand(_named_exact("flamigo"), count=3, reveal=True),
        ),
        Attack(
            title="United Wings",
            game_text="This attack does 20 damage for each Pok\u00e9mon in your discard pile that has the United Wings attack.",
            cost={PokemonTypes.COLORLESS: 2},
            damage=20,
            damage_operator="x",
            effect=unimplemented,
        ),
    ],
)