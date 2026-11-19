from ptcgo.game.card_effects.attacks_common import damage_all_opponents
from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="ca81ed35-044c-5d30-a72d-193432e32496",
    key="PL1",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Giratina.Name",
    display_name="Giratina",
    searchable_by=["Giratina", "Basic", "Giratina"],
    subtypes=["Basic"],
    collector_number=10,
    set_code="PL1",
    rarity=Rarities.RareHolo,
    hp=100,
    elements=[PokemonTypes.PSYCHIC],
    stage=PokemonStage.BASIC,
    retreat_cost=3,
    weakness_type=PokemonTypes.DARKNESS,
    resistance_type=PokemonTypes.COLORLESS,
    family_id=487,
    abilities=[
        Attack(
            title="Over Slash",
            game_text="This attack does 10 damage to each of your opponent's Pok\u00e9mon. (Don't apply Weakness and Resistance for Benched Pok\u00e9mon).",
            cost={PokemonTypes.COLORLESS: 2},
            effect=damage_all_opponents(10),
        ),
        Attack(
            title="Dark Wing Flaps",
            game_text="Choose 1 card from your opponent's hand without looking. Look at the card you chose, then have your opponent shuffle that card into his or her deck.",
            cost={PokemonTypes.PSYCHIC: 2},
            damage=20,
            effect=unimplemented,
        ),
        Attack(
            title="Wrack Down",
            cost={PokemonTypes.PSYCHIC: 1, PokemonTypes.COLORLESS: 2},
            damage=60,
        ),
    ],
)