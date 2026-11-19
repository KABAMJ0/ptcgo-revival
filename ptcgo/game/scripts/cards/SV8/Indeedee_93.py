from ptcgo.game.card_effects.support_common import heal_item
from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented, Triggers
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="e3bcb349-f0e1-5a22-9d14-9a308e69b0a9",
    key="SV8",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Indeedee.Name",
    display_name="Indeedee",
    searchable_by=["Indeedee", "Basic", "Indeedee"],
    subtypes=["Basic"],
    collector_number=93,
    set_code="SV8",
    rarity=Rarities.Uncommon,
    hp=100,
    elements=[PokemonTypes.PSYCHIC],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.DARKNESS,
    resistance_type=PokemonTypes.FIGHTING,
    family_id=876,
    abilities=[
        Ability(
            title="Obliging Heal",
            game_text="When you play this Pok\u00e9mon from your hand onto your Bench during your turn, you may heal 30 damage from your Active Pok\u00e9mon and have it recover from a Special Condition.",
            trigger=Triggers.ON_PLAY,
            effect=heal_item(30, scope="active", condition_cure=True),
        ),
        Attack(
            title="Super Psy Bolt",
            cost={PokemonTypes.PSYCHIC: 1, PokemonTypes.COLORLESS: 1},
            damage=50,
        ),
    ],
)