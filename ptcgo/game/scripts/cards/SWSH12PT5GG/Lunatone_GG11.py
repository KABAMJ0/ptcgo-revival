from ptcgo.game.card_effects.attacks_common import count_energy
from ptcgo.game.card_effects.attacks_common import damage_per
from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities
from ptcgo.game.card_effects.attacks_common import count_energy, damage_per

card = PokemonCardDef(
    guid="5e92f2de-5c9c-52e4-a469-e99a83de3f49",
    key="SWSH12PT5GG",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Lunatone.Name",
    display_name="Lunatone",
    searchable_by=["Lunatone", "Basic", "Lunatone"],
    subtypes=["Basic"],
    collector_number=11,
    set_code="SWSH12PT5GG",
    rarity=Rarities.RareHolo,
    hp=90,
    elements=[PokemonTypes.PSYCHIC],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.DARKNESS,
    resistance_type=PokemonTypes.FIGHTING,
    family_id=337,
    abilities=[
        Attack(
            title="Cycle Draw",
            game_text="Discard a card from your hand. If you do, draw 3 cards.",
            cost={PokemonTypes.PSYCHIC: 1},
            effect=damage_per(count_energy("self", "psychic"), 30),
        ),
        Attack(
            title="Moon Kinesis",
            game_text="This attack does 30 more damage for each Psychic Energy attached to this Pok\u00e9mon.",
            cost={PokemonTypes.COLORLESS: 3},
            damage=30,
            damage_operator="+",
            effect=damage_per(count_energy("self", PokemonTypes.PSYCHIC), per=30, base=30),
        ),
    ],
)