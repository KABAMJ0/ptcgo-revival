from ptcgo.game.card_effects.attacks_common import mill_attack
from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="9bbf92d7-c1b8-5e64-b7c2-78918a2fd26e",
    key="SV3",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Tyranitarex.Name",
    display_name="Tyranitar ex",
    searchable_by=["Tyranitar ex", "Stage 2", "ex", "Tera", "Tyranitarex"],
    subtypes=["Stage 2", "ex", "Tera"],
    collector_number=211,
    set_code="SV3",
    rarity=Rarities.Rare,
    hp=340,
    elements=[PokemonTypes.LIGHTNING],
    stage=PokemonStage.STAGE2,
    retreat_cost=4,
    weakness_type=PokemonTypes.FIGHTING,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Pupitar.Name",
    family_id=246,
    abilities=[
        Attack(
            title="Mountain Hurl",
            game_text="Discard the top 2 cards of your deck.",
            cost={PokemonTypes.FIGHTING: 1},
            damage=120,
            effect=mill_attack(2, opponent=False),
        ),
        Attack(
            title="Lightning Rampage",
            game_text="If your Benched Pok\u00e9mon have any damage counters on them, this attack does 100 more damage.",
            cost={PokemonTypes.FIGHTING: 2},
            damage=150,
            damage_operator="+",
            effect=unimplemented,
        ),
    ],
)