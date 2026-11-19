from ptcgo.game.card_effects.attacks_common import count_energy
from ptcgo.game.card_effects.attacks_common import damage_per
from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="54b8e104-656c-5f9d-b2a6-c0485b0cdca5",
    key="SV1",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Kirlia.Name",
    display_name="Kirlia",
    searchable_by=["Kirlia", "Stage 1", "Kirlia"],
    subtypes=["Stage 1"],
    collector_number=212,
    set_code="SV1",
    rarity=Rarities.Rare,
    hp=90,
    elements=[PokemonTypes.PSYCHIC],
    stage=PokemonStage.STAGE1,
    retreat_cost=1,
    weakness_type=PokemonTypes.DARKNESS,
    resistance_type=PokemonTypes.FIGHTING,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Ralts.Name",
    family_id=280,
    abilities=[
        Attack(
            title="Magical Shot",
            cost={PokemonTypes.PSYCHIC: 1, PokemonTypes.COLORLESS: 1},
            damage=30,
        ),
        Attack(
            title="Psychic",
            game_text="This attack does 20 more damage for each Energy attached to your opponent's Active Pok\u00e9mon.",
            cost={PokemonTypes.PSYCHIC: 2, PokemonTypes.COLORLESS: 1},
            damage=60,
            damage_operator="+",
            effect=damage_per(count_energy("defender"), 20),
        ),
    ],
)