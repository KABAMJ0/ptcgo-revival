from ptcgo.game.card_effects.attacks_common import flip_bonus, self_energy_discard_attack
from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="c01f1490-4dc4-559f-97a2-0627915d9d73",
    key="ME2PT5",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Raichu.Name",
    display_name="Raichu",
    searchable_by=["Raichu", "Stage 1", "Raichu"],
    subtypes=["Stage 1"],
    collector_number=56,
    set_code="ME2PT5",
    rarity=Rarities.Uncommon,
    hp=130,
    elements=[PokemonTypes.LIGHTNING],
    stage=PokemonStage.STAGE1,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIGHTING,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Pikachu.Name",
    family_id=25,
    abilities=[
        Attack(
            title="Quick Blow",
            game_text="Flip a coin. If heads, this attack does 50 more damage.",
            cost={PokemonTypes.LIGHTNING: 1},
            damage=20,
            damage_operator="+",
            effect=flip_bonus(50),
        ),
        Attack(
            title="Strong Volt",
            game_text="Discard a Lightning Energy from this Pok\u00e9mon.",
            cost={PokemonTypes.LIGHTNING: 2, PokemonTypes.COLORLESS: 1},
            damage=150,
            effect=self_energy_discard_attack(count=1, energy_type=PokemonTypes.LIGHTNING),
        ),
    ],
)