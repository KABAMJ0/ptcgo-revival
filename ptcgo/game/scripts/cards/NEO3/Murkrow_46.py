from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities
from ptcgo.game.card_effects.attacks_common import count_bench, flip_damage
from ptcgo.game.card_effects.energies import pokemon_named_like

card = PokemonCardDef(
    guid="3a8dbeeb-5fbe-50ba-b352-5ae0225e37c9",
    key="NEO3",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Murkrow.Name",
    display_name="Murkrow",
    searchable_by=["Murkrow", "Basic", "Murkrow"],
    subtypes=["Basic"],
    collector_number=46,
    set_code="NEO3",
    rarity=Rarities.Common,
    hp=40,
    elements=[PokemonTypes.DARKNESS],
    stage=PokemonStage.BASIC,
    retreat_cost=0,
    resistance_type=PokemonTypes.PSYCHIC,
    family_id=198,
    abilities=[
        Attack(
            title="Call for Family",
            game_text="Search your deck for a Basic Pok\u00e9mon card named Murkrow and put it onto your Bench. Shuffle your deck afterward. (You can't use this attack if your Bench is full.)",
            cost={PokemonTypes.COLORLESS: 1},
            effect=unimplemented,
        ),
        Attack(
            title="Flock Attack",
            game_text="Flip a number of coins equal to the number of Murkrows on your Bench. This attack does 10 damage plus 10 more damage for each heads.",
            cost={PokemonTypes.COLORLESS: 2},
            damage=10,
            damage_operator="+",
            effect=flip_damage(coins_from=count_bench("mine", pokemon_named_like("Murkrow")), base=10, per_heads=10),
        ),
    ],
)