from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities, SpecialConditions
from ptcgo.game.card_effects.attacks_common import condition_attack

card = PokemonCardDef(
    guid="df225ef0-7213-5ae0-89f2-13e567792b94",
    key="SV4PT5",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Oinkologne.Name",
    display_name="Oinkologne",
    searchable_by=["Oinkologne", "Stage 1", "Oinkologne"],
    subtypes=["Stage 1"],
    collector_number=208,
    set_code="SV4PT5",
    rarity=Rarities.Rare,
    hp=130,
    elements=[PokemonTypes.COLORLESS],
    stage=PokemonStage.STAGE1,
    retreat_cost=2,
    weakness_type=PokemonTypes.FIGHTING,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Lechonk.Name",
    family_id=915,
    abilities=[
        Attack(
            title="Finest Selection",
            game_text="Flip 3 coins. Put a number of cards up to the number of heads from your discard pile into your hand.",
            cost={PokemonTypes.COLORLESS: 2},
            effect=unimplemented,
        ),
        Attack(
            title="Perfume Press",
            game_text="Your opponent's Active Pok\u00e9mon is now Confused.",
            cost={PokemonTypes.COLORLESS: 3},
            damage=70,
            effect=condition_attack(SpecialConditions.CONFUSED),
        ),
    ],
)