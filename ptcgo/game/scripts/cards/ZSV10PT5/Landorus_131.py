from ptcgo.game.card_effects.support_common import attach_from_discard
from ptcgo.game.card_effects.trainers import basic_energy_of
from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities
from ptcgo.game.card_effects.support_common import attach_from_discard
from ptcgo.game.card_effects.trainers import basic_energy_of, is_basic_energy_card
from ptcgo.game.card_effects.passives_common import takes_less_passive
from ptcgo.game.card_effects.attacks_common import spread_damage
card = PokemonCardDef(
    guid="b5cce5cb-c926-5eb3-a9e9-354b4d2f5b67",
    key="ZSV10PT5",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Landorus.Name",
    display_name="Landorus",
    searchable_by=["Landorus", "Basic", "Landorus"],
    subtypes=["Basic"],
    collector_number=131,
    set_code="ZSV10PT5",
    rarity=Rarities.Rare,
    hp=130,
    elements=[PokemonTypes.FIGHTING],
    stage=PokemonStage.BASIC,
    retreat_cost=2,
    weakness_type=PokemonTypes.GRASS,
    family_id=645,
    abilities=[
        Attack(
            title="Abundant Harvest",
            game_text="Attach a Basic Fighting Energy card from your discard pile to this Pok\u00e9mon.",
            cost={PokemonTypes.COLORLESS: 1},
            effect=attach_from_discard(basic_energy_of("fighting"), count=1, target="self"),
        ),
        Attack(
            title="Earthquake",
            game_text="This attack also does 10 damage to each of your Benched Pok\u00e9mon. (Don't apply Weakness and Resistance for Benched Pok\u00e9mon.)",
            cost={PokemonTypes.FIGHTING: 1, PokemonTypes.COLORLESS: 2},
            damage=110,
            effect=spread_damage(10, side="mine"),
        ),
    ],
)