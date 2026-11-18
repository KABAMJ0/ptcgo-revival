from ptcgo.game.card_effects.attacks_common import count_in_play, flip_damage
from ptcgo.game.card_effects.trainers import pokemon_of
from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="8e2a14b4-d0cd-5594-9678-42a0582ad9fd",
    key="RSV10PT5",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Scrafty.Name",
    display_name="Scrafty",
    searchable_by=["Scrafty", "Stage 1", "Scrafty"],
    subtypes=["Stage 1"],
    collector_number=58,
    set_code="RSV10PT5",
    rarity=Rarities.Uncommon,
    hp=120,
    elements=[PokemonTypes.DARKNESS],
    stage=PokemonStage.STAGE1,
    retreat_cost=2,
    weakness_type=PokemonTypes.GRASS,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Scraggy.Name",
    family_id=559,
    abilities=[
        Attack(
            title="Ruffians Attack",
            game_text="Flip a coin for each Darkness Pok\u00e9mon you have in play. This attack does 60 damage for each heads.",
            cost={PokemonTypes.DARKNESS: 2},
            damage=60,
            damage_operator="x",
            effect=flip_damage(coins_from=count_in_play("mine", pokemon_of("darkness")), per_heads=60),
        ),
    ],
)
