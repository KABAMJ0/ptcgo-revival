from ptcgo.game.card_effects.attacks_common import snipe_attack
from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="720fb518-62ff-5fea-9531-42c9d49156db",
    key="SV8PT5",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.ScreamTail.Name",
    display_name="Scream Tail",
    searchable_by=["Scream Tail", "Basic", "Ancient", "ScreamTail"],
    subtypes=["Basic", "Ancient"],
    collector_number=42,
    set_code="SV8PT5",
    rarity=Rarities.Uncommon,
    hp=90,
    elements=[PokemonTypes.PSYCHIC],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.DARKNESS,
    resistance_type=PokemonTypes.FIGHTING,
    abilities=[
        Attack(
            title="Slap",
            cost={PokemonTypes.PSYCHIC: 1},
            damage=30,
        ),
        Attack(
            title="Roaring Scream",
            game_text="This attack does 20 damage to 1 of your opponent's Pok\u00e9mon for each damage counter on this Pok\u00e9mon. (Don't apply Weakness and Resistance for Benched Pok\u00e9mon.)",
            cost={PokemonTypes.PSYCHIC: 1, PokemonTypes.COLORLESS: 1},
            effect=snipe_attack(20, pool="any"),
        ),
    ],
)