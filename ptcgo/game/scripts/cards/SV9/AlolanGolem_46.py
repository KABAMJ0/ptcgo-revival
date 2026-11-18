from ptcgo.game.card_effects.attacks_common import recoil_attack
from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="655ee589-9cdf-5a42-bdc3-441b825eb76d",
    key="SV9",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.AlolanGolem.Name",
    display_name="Alolan Golem",
    searchable_by=["Alolan Golem", "Stage 2", "AlolanGolem"],
    subtypes=["Stage 2"],
    collector_number=46,
    set_code="SV9",
    rarity=Rarities.Uncommon,
    hp=180,
    elements=[PokemonTypes.LIGHTNING],
    stage=PokemonStage.STAGE2,
    retreat_cost=4,
    weakness_type=PokemonTypes.FIGHTING,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.AlolanGraveler.Name",
    family_id=74,
    abilities=[
        Attack(
            title="Electromagnetic Catapult",
            game_text="Flip a coin until you get tails. This attack does 70 damage for each heads.",
            cost={PokemonTypes.LIGHTNING: 1},
            damage=70,
            damage_operator="x",
            effect=unimplemented,
        ),
        Attack(
            title="Megaton Fall",
            game_text="This Pok\u00e9mon also does 40 damage to itself.",
            cost={PokemonTypes.LIGHTNING: 1, PokemonTypes.COLORLESS: 1},
            damage=160,
            effect=recoil_attack(40),
        ),
    ],
)