from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities
from ptcgo.game.attributes import SpecialConditions
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities, SpecialConditions
from ptcgo.game.card_effects.attacks_common import condition_attack

card = PokemonCardDef(
    guid="67748930-6103-5622-9f25-e82c0afea1e5",
    key="ECARD2",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Nidoking.Name",
    display_name="Nidoking",
    searchable_by=["Nidoking", "Stage 2", "Nidoking"],
    subtypes=["Stage 2"],
    collector_number=150,
    set_code="ECARD2",
    rarity=Rarities.RareSecret,
    hp=100,
    elements=[PokemonTypes.COLORLESS],
    stage=PokemonStage.STAGE2,
    retreat_cost=3,
    weakness_type=PokemonTypes.GRASS,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Nidorino.Name",
    family_id=32,
    abilities=[
        Ability(
            title="Crystal Type",
            game_text="Whenever you attach a Grass, Lightning, or Fire basic Energy card from your hand to Nidoking, Nidoking's type (color) becomes the same as that Energy card type until the end of the turn.",
            effect=unimplemented,
        ),
        Attack(
            title="Poison Horn",
            game_text="The Defending Pok\u00e9mon is now Poisoned.",
            cost={PokemonTypes.GRASS: 2, PokemonTypes.COLORLESS: 1},
            damage=20,
            effect=condition_attack(SpecialConditions.POISONED),
        ),
        Attack(
            title="Rolling Thunder",
            game_text="Flip a coin, If heads, this attack does 10 damage to each of your opponent's Benched Pok\u00e9mon. If tails, this attack does 10 damage to each of your Benched Pok\u00e9mon. (Don't apply Weakness or Resistance for Benched Pok\u00e9mon.)",
            cost={PokemonTypes.LIGHTNING: 2, PokemonTypes.FIGHTING: 2},
            damage=50,
            effect=unimplemented,
        ),
    ],
)