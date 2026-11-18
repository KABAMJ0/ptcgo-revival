from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from ptcgo.game.card_effects.attacks_common import count_energy, flip_damage
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="1b28c3fc-6840-5439-96e9-0b2b87d2c015",
    key="SV5",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Brambleghast.Name",
    display_name="Brambleghast",
    searchable_by=["Brambleghast", "Stage 1", "Brambleghast"],
    subtypes=["Stage 1"],
    collector_number=21,
    set_code="SV5",
    rarity=Rarities.Rare,
    hp=100,
    elements=[PokemonTypes.GRASS],
    stage=PokemonStage.STAGE1,
    retreat_cost=3,
    weakness_type=PokemonTypes.FIRE,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Bramblin.Name",
    family_id=946,
    abilities=[
        Ability(
            title="Resilient Soul",
            game_text="This Pok\u00e9mon gets +50 HP for each Prize card your opponent has taken.",
            effect=unimplemented,
        ),
        Attack(
            title="Powerful Needles",
            game_text="Flip a coin for each Energy attached to this Pok\u00e9mon. This attack does 80 damage for each heads.",
            cost={PokemonTypes.GRASS: 1, PokemonTypes.COLORLESS: 2},
            damage=80,
            damage_operator="x",
            effect=flip_damage(coins_from=count_energy("self"), per_heads=80, base=0),
        ),
    ],
)