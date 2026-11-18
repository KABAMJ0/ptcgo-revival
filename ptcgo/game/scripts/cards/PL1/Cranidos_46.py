from ptcgo.game.card_effects.attacks_common import flip_damage, flip_gate
from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="903667d6-ed9e-5453-a881-57222d702a8b",
    key="PL1",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Cranidos.Name",
    display_name="Cranidos",
    searchable_by=["Cranidos", "Stage 1", "Cranidos"],
    subtypes=["Stage 1"],
    collector_number=46,
    set_code="PL1",
    rarity=Rarities.Uncommon,
    hp=80,
    elements=[PokemonTypes.FIGHTING],
    stage=PokemonStage.STAGE1,
    retreat_cost=1,
    weakness_type=PokemonTypes.GRASS,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.SkullFossil.Name",
    family_id=408,
    abilities=[
        Attack(
            title="Rock Smash",
            game_text="Flip a coin. If heads, this attack does 20 damage plus 20 more damage.",
            cost={PokemonTypes.FIGHTING: 1},
            damage=20,
            damage_operator="+",
            effect=flip_gate(then=lambda ctx: ctx.deal_damage(40)),
        ),
        Attack(
            title="Knock Over",
            game_text="You may discard any Stadium card in play.",
            cost={PokemonTypes.FIGHTING: 1, PokemonTypes.COLORLESS: 1},
            damage=40,
            effect=unimplemented,
        ),
    ],
)