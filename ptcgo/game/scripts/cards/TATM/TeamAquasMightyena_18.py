from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities
from ptcgo.game.card_effects.attacks_common import count_in_play, flip_damage
from ptcgo.game.card_effects.energies import pokemon_named_like

card = PokemonCardDef(
    guid="770ac1cf-fe03-5ce3-a92c-fe727fc8a6fa",
    key="TATM",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.TeamAquasMightyena.Name",
    display_name="Team Aqua's Mightyena",
    searchable_by=["Team Aqua's Mightyena", "Stage 1", "TeamAquasMightyena"],
    subtypes=["Stage 1"],
    collector_number=18,
    set_code="TATM",
    rarity=Rarities.Common,
    hp=100,
    elements=[PokemonTypes.DARKNESS],
    stage=PokemonStage.STAGE1,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIGHTING,
    resistance_type=PokemonTypes.PSYCHIC,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.TeamAquasPoochyena.Name",
    family_id=261,
    abilities=[
        Attack(
            title="Teampact",
            game_text="Flip a coin for each Team Aqua Pok\u00e9mon you have in play. This attack does 30 damage times the number of heads.",
            cost={PokemonTypes.WATER: 1, PokemonTypes.COLORLESS: 1},
            damage=30,
            damage_operator="x",
            effect=flip_damage(coins_from=count_in_play("mine", pokemon_named_like("Team Aqua's")), per_heads=30),
        ),
        Attack(
            title="Crunch",
            game_text="Flip a coin. If heads, discard an Energy attached to your opponent's Active Pok\u00e9mon.",
            cost={PokemonTypes.WATER: 2, PokemonTypes.COLORLESS: 1},
            damage=80,
            effect=unimplemented,
        ),
    ],
)