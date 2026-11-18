from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from ptcgo.game.card_effects.attacks_common import flip_damage
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="16faa73e-f1b0-5663-aa07-16b8959026bf",
    key="SV9",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Octillery.Name",
    display_name="Octillery",
    searchable_by=["Octillery", "Stage 1", "Octillery"],
    subtypes=["Stage 1"],
    collector_number=34,
    set_code="SV9",
    rarity=Rarities.Uncommon,
    hp=110,
    elements=[PokemonTypes.WATER],
    stage=PokemonStage.STAGE1,
    retreat_cost=2,
    weakness_type=PokemonTypes.LIGHTNING,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Remoraid.Name",
    family_id=223,
    abilities=[
        Attack(
            title="Aqua Wash",
            game_text="You may put an Energy attached to your opponent's Active Pok\u00e9mon into their hand.",
            cost={PokemonTypes.WATER: 1},
            damage=20,
            effect=unimplemented,
        ),
        Attack(
            title="Octo Beatdown",
            game_text="Flip a coin until you get tails. This attack does 90 damage for each heads.",
            cost={PokemonTypes.WATER: 1, PokemonTypes.COLORLESS: 2},
            damage=90,
            damage_operator="x",
            effect=flip_damage(until_tails=True, per_heads=90),
        ),
    ],
)