from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities
from ptcgo.game.card_effects.attacks_common import ignore_modifier_attack

card = PokemonCardDef(
    guid="724bbb1d-9ea0-59ea-a6c1-cdb23bf0981a",
    key="SV3PT5",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Golemex.Name",
    display_name="Golem ex",
    searchable_by=["Golem ex", "Stage 2", "ex", "Golemex"],
    subtypes=["Stage 2", "ex"],
    collector_number=76,
    set_code="SV3PT5",
    rarity=Rarities.Rare,
    hp=330,
    elements=[PokemonTypes.FIGHTING],
    stage=PokemonStage.STAGE2,
    retreat_cost=4,
    weakness_type=PokemonTypes.GRASS,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Graveler.Name",
    family_id=74,
    abilities=[
        Attack(
            title="Dynamic Roll",
            game_text="During your next turn, attacks used by this Pok\u00e9mon do 120 more damage to your opponent's Active Pok\u00e9mon (before applying Weakness and Resistance).",
            cost={PokemonTypes.FIGHTING: 1},
            damage=50,
            effect=unimplemented,
        ),
        Attack(
            title="Rock Blaster",
            game_text="This attack's damage isn't affected by Resistance.",
            cost={PokemonTypes.FIGHTING: 1, PokemonTypes.COLORLESS: 2},
            damage=180,
            effect=ignore_modifier_attack(ignore_resistance=True),
        ),
    ],
)