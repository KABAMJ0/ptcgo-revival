from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities
from ptcgo.game.card_effects.pokemon import UnfazedFatPassive, thumping_snore
card = PokemonCardDef(
    guid="62e43f8e-4d98-5c88-8c32-48cb1f925086",
    key="SWSH11TG",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Snorlax.Name",
    display_name="Snorlax",
    searchable_by=["Snorlax", "Basic", "Snorlax"],
    subtypes=["Basic"],
    collector_number=10,
    set_code="SWSH11TG",
    rarity=Rarities.RareHolo,
    hp=150,
    elements=[PokemonTypes.COLORLESS],
    stage=PokemonStage.BASIC,
    retreat_cost=4,
    weakness_type=PokemonTypes.FIGHTING,
    family_id=143,
    abilities=[
        Ability(
            title="Unfazed Fat",
            game_text="Prevent all effects of attacks from your opponent's Pok\u00e9mon done to this Pok\u00e9mon. (Damage is not an effect.)",
            effect=unimplemented,
        ),
        Attack(
            title="Thumping Snore",
            game_text="This Pok\u00e9mon is now Asleep. During Pok\u00e9mon Checkup, flip 2 coins instead of 1. If either of them is tails, this Pok\u00e9mon is still Asleep.",
            cost={PokemonTypes.COLORLESS: 3},
            damage=180,
            effect=thumping_snore,
        ),
    ],
)